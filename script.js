document.getElementById('loginForm').addEventListener('submit',function(e){
e.preventDefault();
const u=document.getElementById('username').value.trim();
const p=document.getElementById('password').value.trim();
const m=document.getElementById('message');
if(!u||!p){m.style.color='red';m.textContent='Username and Password are required';return;}
if(u==='admin' && p==='password123'){m.style.color='green';m.textContent='Login successful';}
else{m.style.color='red';m.textContent='Invalid username or password';}
});