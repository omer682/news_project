function TimeAndDate(){
    date = new Date()
    time = date.toLocaleTimeString()
    date = date.toDateString();
    TimeDiv = document.getElementById('TimeDiv')
    TimeDiv.innerHTML = `${date}  ${time}`

}

function CustomInterval(func, time){
    setInterval(func, time)

}
