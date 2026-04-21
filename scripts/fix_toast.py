from pathlib import Path

js_path = Path(r'd:\网站开发-json\js\app.js')
content = js_path.read_text(encoding='utf-8')

# Replace the old showToast function with a cleaner version
old = """// === Global Toast Notification ===
window.showToast=function(message,type){
 type=type||'success';
 let toast=document.getElementById('__globalToast');
 if (!toast){
  toast=document.createElement('div');
  toast.id='__globalToast';
  toast.className='toast';
  document.body.appendChild(toast);
 }
 toast.textContent=message;
 toast.className='toast '+type;
 // force reflow to restart transition
 toast.offsetHeight;
 toast.classList.add('show');
 clearTimeout(toast._timer);
 toast._timer=setTimeout(()=>{toast.classList.remove('show');},2800);
};"""

new = """// === Global Toast Notification ===
window.showToast=function(message,type){
 type=(type==='error')?'error':'success';
 let toast=document.getElementById('__globalToast');
 if (!toast){
  toast=document.createElement('div');
  toast.id='__globalToast';
  toast.className='toast';
  document.body.appendChild(toast);
 }
 toast.textContent=message;
 toast.className='toast '+type;
 void toast.offsetHeight;
 toast.classList.add('show');
 clearTimeout(toast._timer);
 toast._timer=setTimeout(function(){toast.classList.remove('show');},2800);
};"""

if old in content:
    content = content.replace(old, new)
    js_path.write_text(content, encoding='utf-8')
    print('showToast function updated')
else:
    print('showToast function not found - checking...')
    # find showToast in content
    idx = content.find('window.showToast')
    print(f'Found at index: {idx}')
    print(repr(content[idx:idx+100]))
