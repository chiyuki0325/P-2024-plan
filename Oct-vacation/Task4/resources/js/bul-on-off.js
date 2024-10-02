function changeImage() {
  const img = document.querySelector('#myimage')
  
  if (img.getAttribute('data-state') === 'off') {
    img.src = './resources/imgs/pic_bulbon.gif'
    img.setAttribute('data-state', 'on')
  } else {
    img.src = './resources/imgs/pic_bulboff.gif'
    img.setAttribute('data-state', 'off')
  }
}
