(function(){
 'use strict';
 function debounce(func,wait){
 let timeout;
 return function(...args){
 clearTimeout(timeout);
 timeout=setTimeout(()=>func.apply(this,args),wait);
};
}
 document.addEventListener('click',function(e){
 const menuToggle=e.target.closest('.menu-toggle');
 if (menuToggle){
 document.querySelector('.navbar-links')?.classList.toggle('show');
}
 const dropdown=e.target.closest('.nav-dropdown');
 if (dropdown&&window.innerWidth<=768){
 e.preventDefault();
 dropdown.classList.toggle('open');
}
 const navLink=e.target.closest('.nav-link');
 if (navLink&&window.innerWidth<=768&&!navLink.closest('.nav-dropdown')){
 document.querySelector('.navbar-links')?.classList.remove('show');
}
},{passive: true});
 const syntaxHighlight=(json)=>{
 if (typeof json!=='string') json=JSON.stringify(json,null,2);
 json=json.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
 return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,(match)=>{
 let cls='json-number';
 if (/^"/.test(match)){
 if (/:$/.test(match)){cls='json-key';match=match.slice(0,-1)+'</span>';return '<span class="'+cls+'">'+match+':';}
 cls='json-string';
 }else if (/true|false/.test(match)){cls='json-boolean';}else if (/null/.test(match)){cls='json-null';}
 return '<span class="'+cls+'">'+match+'</span>';
 });
};
 const $=function(id){return document.getElementById(id);};
 const showMsg=(el,text,type)=>{if (el){el.textContent=text;el.className='message show message-'+type;}};
 const hideMsg=(el)=>{if (el){el.className='message';el.textContent='';}};
 const setStatus=(el,text,valid)=>{if (el){el.innerHTML='<span class="status-dot '+(valid ? 'valid' : 'invalid')+'"></span>'+text;el.className='status-badge '+(valid ? 'success' : 'error');}};
 const showError=(type,message,line)=>{
 const panel=$('errorPanel');
 if (panel){
 $('errorType').textContent=type;
 $('errorMessage').textContent=message;
 $('errorLine').textContent=line ? 'Error at line '+line : '';
 panel.classList.add('show');
 }
 };
 const hideError=function(){$('errorPanel')?.classList.remove('show');};
 const setLoading=(btn,loading)=>{if (!btn) return;if(loading){btn.classList.add('btn-loading');btn.disabled=true;}else{btn.classList.remove('btn-loading');btn.disabled=false;}};
 const getLine=(str,pos)=>{let line=1;for (let i=0;i<pos&&i<str.length;i++) if (str[i]==='\n') line++;return line;};
 const jsonInput=$('jsonInput'),jsonOutput=$('jsonOutput'),jsonHighlight=$('jsonHighlight');
 const formatJSON=()=>{
 const btn=$('btnFormat');
 setLoading(btn,true);
 try{
 const formatted=JSON.stringify(JSON.parse(jsonInput.value),null,2);
 if (jsonOutput) jsonOutput.value=formatted;
 if (jsonHighlight) jsonHighlight.innerHTML=syntaxHighlight(formatted);
 showMsg($('msgFormat'),'JSON formatted successfully!','success');
 setStatus($('statusBadge'),'Valid JSON',true);
 hideError();
 window.showToast('JSON formatted successfully ✓','success');
 }catch (e){
 if (jsonOutput) jsonOutput.value='';
 if (jsonHighlight) jsonHighlight.innerHTML='';
 showMsg($('msgFormat'),'JSON Error: '+e.message,'error');
 setStatus($('statusBadge'),'Invalid JSON',false);
 const m=e.message.match(/position\s+(\d+)/);
 showError('SyntaxError',e.message,m ? getLine(jsonInput.value,parseInt(m[1])) : null);
 }
 setLoading(btn,false);
 };
 const validateJSON=()=>{
 const btn=$('btnValidate');
 setLoading(btn,true);
 try{
 JSON.parse(jsonInput.value);
 showMsg($('msgFormat'),'Valid JSON!','success');
 setStatus($('statusBadge'),'Valid JSON',true);
 hideError();
 }catch (e){
 showMsg($('msgFormat'),'JSON Error: '+e.message,'error');
 setStatus($('statusBadge'),'Invalid JSON',false);
 const m=e.message.match(/position\s+(\d+)/);
 showError('SyntaxError',e.message,m ? getLine(jsonInput.value,parseInt(m[1])) : null);
 }
 setLoading(btn,false);
 };
 const compressJSON=()=>{
 const btn=$('btnCompress');
 setLoading(btn,true);
 try{
 const compressed=JSON.stringify(JSON.parse(jsonInput.value));
 if (jsonOutput) jsonOutput.value=compressed;
 if (jsonHighlight) jsonHighlight.innerHTML=syntaxHighlight(compressed);
 showMsg($('msgFormat'),'JSON compressed successfully!','success');
 hideError();
 window.showToast('JSON minified successfully ✓','success');
 }catch (e){
 showMsg($('msgFormat'),'Cannot compress: '+e.message,'error');
 showError('SyntaxError',e.message,null);
 }
 setLoading(btn,false);
 };
 $('btnFormat')?.addEventListener('click',formatJSON);
 $('btnValidate')?.addEventListener('click',validateJSON);
 $('btnCompress')?.addEventListener('click',compressJSON);

 // === COPY BUTTON (FIXED: copy the correct output per page) ===
 $('btnCopy')?.addEventListener('click',async function(){
 let output='';
 if (jsonOutput) output=jsonOutput.value;
 else if ($('extractOutput')) output=$('extractOutput').value;
 else if ($('escapeOutput')) output=$('escapeOutput').value;
 if (output){
 try{
 await navigator.clipboard.writeText(output);
 const orig=this.innerHTML;
 this.innerHTML='✓ Copied';
 window.showToast('Copied to clipboard ✓','success');
 setTimeout(()=>{this.innerHTML=orig;},2000);
 }catch (err){console.error('Copy failed:',err);}
 }else{
 window.showToast('Nothing to copy','error');
 }
 });

 // === CLEAR BUTTON (FIXED: clear the correct fields per page) ===
 $('btnClear')?.addEventListener('click',function(){
 // Formatter page
 if (jsonInput) jsonInput.value='';
 if (jsonOutput) jsonOutput.value='';
 if (jsonHighlight) jsonHighlight.innerHTML='';
 hideMsg($('msgFormat'));
 hideError();
 if ($('statusBadge')) $('statusBadge').innerHTML='';
 // Extract page
 const extractInput=$('extractInput');
 const extractOutput=$('extractOutput');
 const extractHighlight=$('extractHighlight');
 const pathInput=$('pathInput');
 const msgExtract=$('msgExtract');
 if (extractInput) extractInput.value='';
 if (extractOutput) extractOutput.value='';
 if (extractHighlight) extractHighlight.innerHTML='';
 if (pathInput) pathInput.value='';
 hideMsg(msgExtract);
 // Escape page
 const escapeInput=$('escapeInput');
 const escapeOutput=$('escapeOutput');
 const escapeHighlight=$('escapeHighlight');
 const msgEscape=$('msgEscape');
 if (escapeInput) escapeInput.value='';
 if (escapeOutput) escapeOutput.value='';
 if (escapeHighlight) escapeHighlight.innerHTML='';
 hideMsg(msgEscape);
 });

 if (jsonInput){
 jsonInput.addEventListener('input',debounce(function(){
 const input=jsonInput.value;
 if (!input.trim()){
 if (jsonHighlight) jsonHighlight.innerHTML='';
 if ($('statusBadge')) $('statusBadge').innerHTML='';
 hideError();
 return;
 }
 try{
 if (jsonHighlight) jsonHighlight.innerHTML=syntaxHighlight(JSON.stringify(JSON.parse(input),null,2));
 setStatus($('statusBadge'),'Valid JSON',true);
 hideError();
 }catch (e){
 if (jsonHighlight) jsonHighlight.innerHTML='<span style="color: var(--error)">Invalid: '+e.message+'</span>';
 setStatus($('statusBadge'),'Invalid JSON',false);
 const m=e.message.match(/position\s+(\d+)/);
 showError('SyntaxError',e.message,m ? getLine(input,parseInt(m[1])) : null);
 }
 },300));
 }
 const escapeInput=$('escapeInput'),escapeOutput=$('escapeOutput'),escapeHighlight=$('escapeHighlight');
 $('btnEscape')?.addEventListener('click',function(){
 if (!escapeInput) return;
 const escaped=JSON.stringify(escapeInput.value).slice(1,-1);
 if (escapeOutput) escapeOutput.value=escaped;
 if (escapeHighlight) escapeHighlight.innerHTML=escaped;
 showMsg($('msgEscape'),'String escaped!','success');
 });
 $('btnUnescape')?.addEventListener('click',function(){
 if (!escapeInput) return;
 try{
 const unescaped=JSON.parse('"'+escapeInput.value+'"');
 if (escapeOutput) escapeOutput.value=unescaped;
 if (escapeHighlight) escapeHighlight.innerHTML=unescaped;
 showMsg($('msgEscape'),'String unescaped!','success');
 }catch (e){showMsg($('msgEscape'),'Unescape failed: '+e.message,'error');}
 });
 const extractByPath=(obj,path)=>{
 let result=obj;
 path=path.replace(/^\$?\.?/,'');
 if (!path) return result;
 const parts=path.split(/\.|\[|\]/).filter(function(p){return p;});
 for (const part of parts){
 if (result&&typeof result==='object'){
 if (part.endsWith(']')){
 const index=parseInt(part.match(/\[(\d+)\]/)?.[1]||'0',10);
 result=Array.isArray(result) ? result[index] : result[part.slice(0,-1)]?.[index];
 }else{result=result[part];}
 }
 if (result===undefined) throw new Error('Path not found: '+path);
 }
 return result;
 };
 $('btnExtract')?.addEventListener('click',function(){
 try{
 const parsed=JSON.parse($('extractInput').value);
 const result=extractByPath(parsed,$('pathInput').value);
 const formatted=JSON.stringify(result,null,2);
 if ($('extractOutput')) $('extractOutput').value=formatted;
 if ($('extractHighlight')) $('extractHighlight').innerHTML=syntaxHighlight(formatted);
 showMsg($('msgExtract'),'Extraction successful!','success');
 }catch (e){showMsg($('msgExtract'),'Extraction failed: '+e.message,'error');}
 });

 // === TEMPLATES (FIXED: separate templates per page + example0/1/2 keys) ===
 const formatterTemplates={
 api: '{"success":true,"data":{"id":1001,"name":"Example","email":"test@example.com"}}',
 user: '{"user":{"id":"u123","role":"admin","verified":true,"preferences":{"theme":"dark"}}}',
 product: '{"products":[{"id":"P001","name":"iPhone","price":999},{"id":"P002","name":"MacBook","price":1299}]}',
 package: '{"name":"my-app","version":"1.0.0","dependencies":{"express":"^4.18"}}',
 i18n: '{"en":{"welcome":"Hello"},"zh":{"welcome":"你好"}}'
 };
 const extractTemplates={
 example0: '{"name":"Alice","age":30,"address":{"city":"New York","zip":"10001"},"skills":["JS","Python"],"projects":[{"name":"Project A","status":"Done"},{"name":"Project B","status":"WIP"}]}',
 example1: '{"users":[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"},{"id":3,"name":"Carol"}]}',
 example2: '{"company":{"departments":[{"name":"Engineering","headcount":50},{"name":"Marketing","headcount":12}]}}}'
 };
 const escapeTemplates={
 example0: '{"message":"Hello \\"World\\"","special":"Tab:\\tNewLine:\\n"}',
 example1: 'Line one\\nLine two\\tWith tabs',
 example2: 'Path: C:\\\\Users\\\\John\\\\Documents\\\\File.txt'
 };
 $('templateSelect')?.addEventListener('change',function(){
 if (!this.value) return;
 // Formatter page
 if ($('jsonInput')&&formatterTemplates[this.value]){
 $('jsonInput').value=formatterTemplates[this.value];
 $('btnFormat')?.click();
 showMsg($('msgFormat'),'Template loaded','success');
 }
 // Extract page
 else if ($('extractInput')&&extractTemplates[this.value]){
 $('extractInput').value=extractTemplates[this.value];
 showMsg($('msgExtract'),'Example loaded','success');
 }
 // Escape page
 else if ($('escapeInput')&&escapeTemplates[this.value]){
 $('escapeInput').value=escapeTemplates[this.value];
 showMsg($('msgEscape'),'Example loaded','success');
 }
 this.value='';
 });
 if ('IntersectionObserver' in window){
 const observer=new IntersectionObserver(function(entries,obs){
 entries.forEach(function(entry){
 if (entry.isIntersecting){
 const img=entry.target;
 if (img.dataset.src){img.src=img.dataset.src;img.removeAttribute('data-src');img.classList.add('loaded');}
 obs.unobserve(img);
 }
 });
 },{rootMargin: '50px 0px'});
 document.querySelectorAll('img[data-src]').forEach(function(img){observer.observe(img);});
 }
 // === Global Toast Notification ===
 window.showToast=function(message,type){
 type=(type==='error')?'error':'success';
 let toast=document.getElementById('__globalToast');
 if (!toast){
 toast=document.createElement('div');
 toast.id='__globalToast';
 toast.className='toast center';
 document.body.appendChild(toast);
 }
 toast.textContent=message;
 toast.className='toast center '+type;
 void toast.offsetHeight;
 toast.classList.add('show');
 clearTimeout(toast._timer);
 toast._timer=setTimeout(function(){toast.classList.remove('show');},2800);
 };
})();
