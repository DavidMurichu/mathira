
function toggle(name){
  event.preventDefault();
  name1=name+'_approved';
  var table=document.getElementById(name);
  var table1=document.getElementById(name1);
  console.log(name)
  console.log(name1)

  if (table.style.display === 'none'){
    table.style.display='';
    table1.style.display= 'none';
    localStorage.setItem('lastTable', '');
  }else{
    table.style.display='none';
    table1.style.display= '';
    localStorage.setItem('lastTable', 'table1');

  }
}
function setdisp(){
  var lastTable=localStorage.getItem('lastTable')
  if(lastTable==='table1'){
    table.style.display='none';
    table1.style.display=''
  }
}
window.onload=setdisp;

