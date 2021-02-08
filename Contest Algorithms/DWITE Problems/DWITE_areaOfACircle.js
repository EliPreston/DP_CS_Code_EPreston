


// function circleArea {


    x1 = 2
    x2 = 4
    y1 = 4
    y2 = 8


    r = Math.pow((y2-y1)*(y2-y1) + (x2 - x1)*(x2 - x1), 1/2)
    a = 3.14159*r*r

    // a = Math.round(a) --> Rounds without any decimals
    // a = a.toPrecision(5) --> Significant figures
    // a = toFixed(3) --> Fixed number of decimal places


    a = a*1000
    a = Math.round(a)
    a = a/1000


    console.log(a)
// }