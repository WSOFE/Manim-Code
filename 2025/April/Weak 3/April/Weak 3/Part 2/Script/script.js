console.log(window.innerHeight);
console.log(window.innerWidth);
let btnAll = document.querySelectorAll(".download");
let clicked;
console.log(btnAll);



function latexFunction(classname,latex){
  let write = document.querySelector(`.${classname}`);
  
  katex.render(latex,write);
  // katex.render(String.raw`${latex}`,write,{
  //   throwOnError: false
  // });
}
// document.querySelector(".latex").addEventListener("click",function(){
//   latexFunction("L",);
// });
window.addEventListener("DOMContentLoaded",function(){
  let allSpan = this.document.querySelectorAll("span");
  console.log(allSpan);
  
  for(let i=0;i<l.length;i++){
    latexFunction(`L${i}`,l[i]);
  }
})
console.log(l);

















btnAll.forEach(btn => {
  btn.addEventListener("click",() =>{
    clicked = btn.id;
    console.log(btn.id);
    let images = document.querySelector(`.${clicked}`);

    html2canvas(images).then(canvas =>{
                
      var link = document.createElement("a");
      link.download = `${Math.random()}.png`;
      link.href = canvas.toDataURL();
      link.click();
      console.log(link);

      

  });
  })
}) 

