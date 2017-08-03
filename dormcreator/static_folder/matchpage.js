var slideIndex = 0;
var timer = 0
function showSlides() {
    clearTimeout(timer)
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex> slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    timer = setTimeout(showSlides, 5000); // Change image every 5 seconds
}

$(document).ready(function(){
  $(".image").click(showSlides)
  showSlides()
})
