import {createContext,useContext} from 'react';
import type {AppState,Word,Paper} from './types';
import type {ContentBank} from './content-updates';
export interface ModelConfig {endpoint:string;model:string;key:string;enabled:boolean}
export interface ContextValue {state:AppState;update:(fn:(s:AppState)=>void)=>void;replace:(s:AppState)=>void;notify:(s:string)=>void;allWords:Word[];allPapers:Paper[];model:ModelConfig;setModel:(v:ModelConfig)=>void;content:ContentBank;checkUpdates:()=>Promise<void>;updateStatus:string}
export const AppContext=createContext<ContextValue>(null!);
export const useApp=()=>useContext(AppContext);
export const go=(page:string)=>{location.hash=page;window.scrollTo({top:0,behavior:'smooth'});};
export async function copyText(text:string){await navigator.clipboard.writeText(text);}
export function speak(text:string){if(!('speechSynthesis' in window))return false;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(text);u.lang='en-GB';u.rate=.88;speechSynthesis.speak(u);return true;}
