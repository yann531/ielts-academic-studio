export type Skill='listening'|'reading';
export interface Question {id:string;type:'text'|'select';prompt:string;answers:string[];options?:string[];maxWords?:number;explanation:string;evidence:string;paraphrase?:string;trap?:string;paragraph?:string}
export interface Passage {id:string;title:string;paragraphs:{label:string;text:string}[];questions:Question[];audio?:string;audioKind?:string;duration?:number;visual?:{title:string;grid:string[][]}}
export interface Paper {id:string;skill:Skill;title:string;subtitle:string;minutes:number;source:string;kind:string;review:string;updated:string;difficulty:string;passages:Passage[]}
export interface Resource {id:string;title:string;publisher:string;official:boolean;skills:string[];stage:string;language:string;cost:string;account:string;url:string;checked:string;reason:string;format:string}
export interface Word {id:string;term:string;pos:string;meaning:string;topic:string;collocation:string;example:string;register:string;error:string;kind:'word'|'phrase';source:string;pronunciation?:string;collocations?:{text:string;meaning:string}[];examples?:{text:string;translation:string}[];forms?:string[];tags?:string[];sources?:{title:string;url:string;kind:'reference'|'lookup'}[];retired?:boolean;retirementReason?:string;spellingVariants?:string[];contentVersion?:string}
export type VocabMark='unmarked'|'again'|'ok'|'archived';
export interface VocabProgress {status:VocabMark;statusAt:number;forget:boolean;forgetAt:number;firstLearned?:string;lastReview?:string;nextReview?:string;reviewCount:number;updated:number;legacy?:string}
export interface VocabDay {date:string;limit:number;newIds:string[];newDone:string[];excludedIds?:string[];reviewIds:string[];reviewDone:string[];sources:Record<string,string[]>;created:number;updated:number}
export interface VocabTestAnswer {wordId:string;input:string;correct:boolean|null;at:number}
export interface VocabTest {id:string;date:string;scope:string;mode:'meaning'|'spelling';order:string[];answers:VocabTestAnswer[];started:number;updated:number;finished?:number;draft?:{wordId:string;input:string;revealed:boolean}}
export interface VocabularyState {version:1;migrated:boolean;progress:Record<string,VocabProgress>;tasks:Record<string,{origin:string;doneAt?:string}>;days:Record<string,VocabDay>;tests:VocabTest[];events:{id:string;wordId:string;at:number;action:string}[]}
export interface WritingTask {id:string;task:1|2;type:string;title:string;prompt:string;chart?:{kind:string;labels:string[];series:{name:string;values:number[]}[];unit:string};visual?:string;analysis:string;ideas:string[];outline:string[];sample?:string;expressions:string[];errors:string[];source:string;review:string;updated:string}
export interface SpeakingTopic {id:string;title:string;p1:string[];p2:string;p2points:string[];p3:string[];ideas:string[];phrases:string[];source:string}
export interface Card {due:number;interval:number;ease:number;reps:number;lapses:number;status:'learning'|'mastered'|'suspended';updated:number}
export interface Attempt {id:string;paperId:string;skill:Skill;at:number;answers:Record<string,string>;correct:number;total:number;mistakes:string[];mode:string}
export interface Session {scope?:string;paperId:string;answers:Record<string,string>;started:number;deadline:number;mode:'practice'|'exam';submitted:boolean;part:number;played:string[];audioTimes:Record<string,number>}
export interface Draft {id:string;text:string;updated:number;history:{text:string;at:number}[];feedback?:string;deadline?:number;submitted?:boolean}
export interface Recording {id:string;topic:string;at:number;name:string;mime:string;data:string}
export interface LibraryFile {id:string;name:string;mime:string;data:string;at:number}
export interface AppState {version:1;updated:number;sessions:Record<string,Session>;attempts:Attempt[];drafts:Record<string,Draft>;cards:Record<string,Card>;customWords:Word[];customPapers:Paper[];notes:Record<string,string>;highlights:Record<string,string[]>;recordings:Recording[];files:LibraryFile[];reviews:{id:string;wordId:string;rating:string;at:number}[];settings:{dailyNew:number;target:string};completed:string[];vocabulary?:VocabularyState}
