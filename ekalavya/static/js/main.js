document.addEventListener("DOMContentLoaded",function(){

let slides=document.querySelectorAll(".hero-slide")
let indicators=document.querySelectorAll(".indicator")

let index=0

function showSlide(i){

if(slides.length===0||indicators.length===0)return

slides.forEach(s=>s.classList.remove("active"))
indicators.forEach(s=>s.classList.remove("active"))

if(slides[i])slides[i].classList.add("active")
if(indicators[i])indicators[i].classList.add("active")

}

function next(){

if(slides.length===0)return

index++
if(index>=slides.length){index=0}
showSlide(index)

}

function prev(){

if(slides.length===0)return

index--
if(index<0){index=slides.length-1}
showSlide(index)

}

document.getElementById("nextSlide")?.addEventListener("click",next)
document.getElementById("prevSlide")?.addEventListener("click",prev)

if(slides.length>0){
setInterval(next,5000)
}

indicators.forEach((dot,i)=>{

dot.addEventListener("click",()=>{

index=i
showSlide(index)

})

})


/* VIDEO MODAL */

const modal=document.getElementById("videoModal")
const trigger=document.getElementById("videoTrigger")
const closeBtn=document.getElementById("closeVideo")
const frame=document.getElementById("videoFrame")
const videoPlayer=document.getElementById("videoPlayer")

trigger?.addEventListener("click",()=>{

modal.style.display="flex"
if(frame){
frame.src=frame.dataset.src || ""
}
if(videoPlayer){
videoPlayer.play()
}

})

closeBtn?.addEventListener("click",()=>{

modal.style.display="none"
if(frame){
frame.src=""
}
if(videoPlayer){
videoPlayer.pause()
videoPlayer.currentTime=0
}

})


/* FUNNEL ACCORDION */

const funnelCards=document.querySelectorAll(".funnel-card")

funnelCards.forEach(card=>{
const header=card.querySelector(".funnel-card-header")
header?.addEventListener("click",()=>{
// Close all other cards
funnelCards.forEach(c=>{
if(c!==card){
c.classList.remove("active")
}
})
// Toggle current card
card.classList.toggle("active")
})
})

})