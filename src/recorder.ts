// Shared by the Speaking page and the synthetic-audio browser test.
export function makeRecorder(stream:MediaStream,onData:(blob:Blob)=>void,onStopped:()=>void,onError:()=>void){
 const mime=['audio/webm;codecs=opus','audio/mp4','audio/webm'].find(x=>MediaRecorder.isTypeSupported(x));
 const recorder=new MediaRecorder(stream,mime?{mimeType:mime}:undefined),chunks:Blob[]=[];
 recorder.ondataavailable=e=>{if(e.data.size)chunks.push(e.data);};
 recorder.onstop=()=>{onData(new Blob(chunks,{type:recorder.mimeType}));onStopped();};
 recorder.onerror=onError;
 return recorder;
}
