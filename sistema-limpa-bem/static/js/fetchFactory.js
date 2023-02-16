function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

async function fetchFactory(method, url, body) {
    let dataReturned
    let init = {
        method: method,
        headers: {},
    }
    if (method == 'GET') {
        init.headers = {
            'X-CSRFToken': getCookie("csrftoken")
        }
    } else {
        init.headers = {
            'X-CSRFToken': getCookie("csrftoken"),
            'Content-Type': 'application/json'
        }
        init = Object.assign(init, { body: JSON.stringify(body) })
    }
    await fetch(url, init)
        .then(response => response.json())
        .then(dataResponse => dataReturned = dataResponse)
    return dataReturned
}