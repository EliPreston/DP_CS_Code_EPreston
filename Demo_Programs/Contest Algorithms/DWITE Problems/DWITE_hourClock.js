

function calculate12hour() {

    time = "12:30"

    h = time.substring(0,2)
    h = parseInt(h)

    m = time.substring(3, 5)


    x = "AM"

    if ( h >= 12 && h <= 23) {
        x = "PM"
        h = h - 12
    } else if (h == 00) {
        h = 12
    }

    console.log(h + ":" + m + " " + x)
}