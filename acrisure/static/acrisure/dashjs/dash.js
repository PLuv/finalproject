// dashboard.html js functions
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#policy_cancel').onsubmit = () => {
        // initialize new request
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/policy_cancel');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        // Callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            var len = data.data.length;
            if (len > 0) {
                const template = Handlebars.compile(document.querySelector('#cnx_policy_script').innerHTML);
                var policies = [];
                for (let i = 0; i < len; i++) {
                    policies.push(data.data[i].policy_number);
                }
                // Add policy choices to DOM
                const content = template({'policies': policies});
                document.querySelector('#cnx_policy_div').innerHTML += content;
            }
            else {
                alert("There has been an error, please reload dashboard and try again.");
            }
        };

        // add data to send & send request
        const data = new FormData();
        var id_accounts = document.querySelector('#id_accounts').value;
        data.append('account_choice', id_accounts);
        data.append('meta', 0);
        request.send(data);
        return false;
    };

    // if cnx_policy submitted - process.
    document.querySelector('#cnx_policy').onsubmit = () => {
        // initialize request
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/policy_cancel');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        // Callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success) {
                alert(`"Policy expiration date set to ${data.exp}"`);
                document.querySelector('#cnx_close').click();
            }
            else {
                alert("ooops something went wrong. Please reload dashboard and try again");
            }
        };
        // add data to send & send request
        const data = new FormData();
        var id_cnx_pol = document.querySelector('#id_cnx_pol').value;
        var new_expiration_date = document.querySelector('#new_expiration_date').value;
        data.append('cnx_policy_choice', id_cnx_pol);
        data.append('new_expiration_date', new_expiration_date);
        data.append('meta', 1);
        request.send(data);
        return false;
    };
});

// Find the CSRF Token cookie value
function parse_cookies() {
    var cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}
