var dialog,iframe;
function onMovieClick(e)
{
  var url = this.getAttribute("data-url")
  var id = url.split('=')
  url = id.length  > 1 ? id[1] : undefined
  iframe.src = "https://www.youtube.com/embed/"+url+"?autoplay=1"
  dialog.style.display = 'block'
}
window.onload = function(){
  var movieList = document.querySelectorAll('.movie')
  for(var i = 0; i < movieList.length; i++)
    movieList[i].onclick = onMovieClick;
  dialog = document.querySelector('.dialog')
  iframe = document.querySelector('.movie-trailer')
  dialog.onclick = function(e){
    if(e.target === this)
    {
      this.style.display = 'none'
      iframe.src = "#"
    }

  }
}
