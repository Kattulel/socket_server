setInterval(function myFunction(){
  mudar_texto_vavs()
}, 100);

function mudar_texto_vavs() {
    var x = Math.floor(Math.random() * 256);
    var y = 100+ Math.floor(Math.random() * 256);
    var z = 50+ Math.floor(Math.random() * 256);
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
    console.log(bgColor)
    document.getElementById("vavs").style.color = bgColor;
}