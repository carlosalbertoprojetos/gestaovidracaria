     //janeiro  
    let d1 = toDate("01/01/2022"),
    d2 = toDate("31/01/2022"),
    intervalos1 = [];    
    intervalos1.push( toString(d1) );

    while ( d1 < d2 ) {
    d1.setDate( d1.getDate() + 1 );
    intervalos1.push( toString(d1) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }
    //fevereiro
    let d3 = toDate("01/02/2022"),
    d4 = toDate("28/02/2022"),
    intervalos2 = [];

    intervalos2.push( toString(d3) );

    while ( d3 < d4 ) {
    d3.setDate( d3.getDate() + 1 );
    intervalos2.push( toString(d3) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //março
    let d5 = toDate("01/03/2022"),
    d6 = toDate("31/03/2022"),
    intervalos3 = [];

    intervalos3.push( toString(d5) );

    while ( d5 < d6 ) {
    d5.setDate( d5.getDate() + 1 );
    intervalos3.push( toString(d5) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }

    //abril
    let d7 = toDate("01/04/2022"),
    d8 = toDate("30/04/2022"),
    intervalos4 = [];

    intervalos4.push( toString(d7) );

    while ( d7 < d8 ) {
    d7.setDate( d7.getDate() + 1 );
    intervalos4.push( toString(d7) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    }
    //maio
    let d9 = toDate("01/05/2022"),
    d10 = toDate("31/05/2022"),
    intervalos5 = [];

    intervalos5.push( toString(d9) );

    while ( d9 < d10 ) {
    d9.setDate( d9.getDate() + 1 );
    intervalos5.push( toString(d9) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //junho
    let d11 = toDate("01/06/2022"),
    d12 = toDate("30/06/2022"),
    intervalos6 = [];

    intervalos6.push( toString(d11) );

    while ( d11 < d12 ) {
    d11.setDate( d11.getDate() + 1 );
    intervalos6.push( toString(d11) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    //julho
    
    let d13 = toDate("01/07/2022"),
    d14 = toDate("31/07/2022"),
    intervalos7 = [];

    intervalos7.push( toString(d13) );

    while ( d13 < d14 ) {
    d13.setDate( d13.getDate() + 1 );
    intervalos7.push( toString(d13) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //agosto
   
    let d15 = toDate("01/08/2022"),
    d16 = toDate("31/08/2022"),
    intervalos8 = [];

    intervalos8.push( toString(d15) );

    while ( d15 < d16 ) {
    d15.setDate( d15.getDate() + 1 );
    intervalos8.push( toString(d15) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
    //setembro
    
    let d17 = toDate("01/09/2022"),
    d18 = toDate("30/09/2022"),
    intervalos9 = [];

    intervalos9.push( toString(d17) );

    while ( d17 < d18 ) {
    d17.setDate( d17.getDate() + 1 );
    intervalos9.push( toString(d17) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    
    //outubro
    
    let d19 = toDate("01/10/2022"),
    d20 = toDate("31/10/2022"),
    intervalos10 = [];

    intervalos10.push( toString(d19) );

    while ( d19 < d20 ) {
    d19.setDate( d19.getDate() + 1 );
    intervalos10.push( toString(d19) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    
    //novembro
    
    let d21 = toDate("01/11/2022"),
    d22 = toDate("30/11/2022"),
    intervalos11 = [];

    intervalos11.push( toString(d21) );

    while ( d21 < d22 ) {
    d21.setDate( d21.getDate() + 1 );
    intervalos11.push( toString(d21) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 

    
    //dezembro 2022
    
    let d23 = toDate("01/12/2022"),
    d24 = toDate("31/12/2022"),
    intervalos12 = [];

    intervalos12.push( toString(d23) );

    while ( d23 < d24 ) {
    d23.setDate( d23.getDate() + 1 );
    intervalos12.push( toString(d23) );
    }
    function toDate(texto) {
        let partes = texto.split('/');
        return new Date(partes[2], partes[1]-1, partes[0]);
    }

    function toString(date) {
        return ('0' + date.getDate()).slice(-2) + '/' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
        date.getFullYear();
    } 
    
//======================================================================
//janeiro 2023
    
let d25 = toDate("01/01/2023"),
d26 = toDate("31/01/2023"),
intervalos13 = [];

intervalos13.push( toString(d25) );

while ( d25 < d26 ) {
d25.setDate( d25.getDate() + 1 );
intervalos13.push( toString(d25) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 

//fevereiro 2023
let d27 = toDate("01/02/2023"),
d28 = toDate("28/02/2023"),
intervalos14 = [];

intervalos14.push( toString(d27) );

while ( d27 < d28 ) {
d27.setDate( d27.getDate() + 1 );
intervalos14.push( toString(d27) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
}

//março
let d29 = toDate("01/03/2023"),
d30 = toDate("31/03/2023"),
intervalos15 = [];

intervalos15.push( toString(d29) );

while ( d29 < d30 ) {
d29.setDate( d29.getDate() + 1 );
intervalos15.push( toString(d29) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
}

//abril
let d31 = toDate("01/04/2023"),
d32 = toDate("30/04/2023"),
intervalos16 = [];

intervalos16.push( toString(d31) );

while ( d31 < d32 ) {
d31.setDate( d31.getDate() + 1 );
intervalos16.push( toString(d31) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
}
//maio
let d33 = toDate("01/05/2023"),
d34 = toDate("31/05/2023"),
intervalos17 = [];

intervalos17.push( toString(d33) );

while ( d33 < d34 ) {
d33.setDate( d33.getDate() + 1 );
intervalos17.push( toString(d33) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 

//junho
let d35 = toDate("01/06/2023"),
d36 = toDate("30/06/2023"),
intervalos18 = [];

intervalos18.push( toString(d35) );

while ( d35 < d36 ) {
d35.setDate( d35.getDate() + 1 );
intervalos18.push( toString(d35) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 

//julho

let d37 = toDate("01/07/2023"),
d38 = toDate("31/07/2023"),
intervalos19 = [];

intervalos19.push( toString(d37) );

while ( d37 < d38 ) {
d37.setDate( d37.getDate() + 1 );
intervalos19.push( toString(d37) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 

//agosto

let d39 = toDate("01/08/2023"),
d40 = toDate("31/08/2023"),
intervalos20 = [];

intervalos20.push( toString(d39) );

while ( d39 < d40 ) {
d39.setDate( d39.getDate() + 1 );
intervalos20.push( toString(d39) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 

//setembro

let d41 = toDate("01/09/2023"),
d42 = toDate("30/09/2023"),
intervalos21 = [];

intervalos21.push( toString(d41) );

while ( d41 < d42 ) {
d41.setDate( d41.getDate() + 1 );
intervalos21.push( toString(d41) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 


//outubro

let d43 = toDate("01/10/2023"),
d44 = toDate("31/10/2023"),
intervalos22 = [];

intervalos22.push( toString(d43) );

while ( d43 < d44 ) {
d43.setDate( d43.getDate() + 1 );
intervalos22.push( toString(d43) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 


//novembro

let d45 = toDate("01/11/2023"),
d46 = toDate("30/11/2023"),
intervalos23 = [];

intervalos23.push( toString(d45) );

while ( d45 < d46 ) {
d45.setDate( d45.getDate() + 1 );
intervalos23.push( toString(d45) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 


//dezembro 2022

let d47 = toDate("01/12/2023"),
d48 = toDate("31/12/2023"),
intervalos24 = [];

intervalos24.push( toString(d47) );

while ( d47 < d48 ) {
d47.setDate( d47.getDate() + 1 );
intervalos24.push( toString(d47) );
}
function toDate(texto) {
    let partes = texto.split('/');
    return new Date(partes[2], partes[1]-1, partes[0]);
}

function toString(date) {
    return ('0' + date.getDate()).slice(-2) + '/' +
    ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
    date.getFullYear();
} 