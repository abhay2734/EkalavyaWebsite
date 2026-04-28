document.addEventListener("DOMContentLoaded",function(){

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


})
