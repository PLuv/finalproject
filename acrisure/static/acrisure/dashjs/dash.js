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

    // Vehicle delete code:
    document.querySelector('#vehicle_dlt').onsubmit = () => {
        // initialize new request
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/veh_delete');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        // Callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            var len = data.data.length;
            if (len > 0){
                const template = Handlebars.compile(document.querySelector('#sel_policy_script').innerHTML);
                var policies = [];
                for (let i = 0; i < len; i++) {
                    policies.push(data.data[i].policy_number);
                }
                // add policy choices to DOM
                const content = template({'policies': policies});
                document.querySelector('#sel_policy_div').innerHTML += content;
            }
            else {
                alert("There has been an error, please reload dashboard and try again.");
            }
        };

        // add data & send
        const data = new FormData();
        var id_for_accounts = document.querySelector('#id_for_accounts').value;
        data.append('account_choice', id_for_accounts);
        data.append('meta', 0);
        request.send(data);
        return false;
    };

    // get vehicles from selected policy
    document.querySelector('#sel_pol').onsubmit = () => {
        // initialize Request
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/veh_delete');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        // callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            var len = data.data.length;
            if (len > 0) {
                const template = Handlebars.compile(document.querySelector('#sel_veh_script').innerHTML);
                var vehicles = [];
                for (let i = 0; i < len; i++) {
                    vehicles.push(data.data[i].vin);
                }
                // add Vehicle choices to DOM
                const content = template({'vehicles': vehicles});
                document.querySelector('#veh_sel_div').innerHTML += content;
            }
        };
        // add data to send
        const data = new FormData();
        var id_sel_pol = document.querySelector('#id_sel_pol').value;
        data.append('id_sel_pol', id_sel_pol);
        data.append('meta', 1);
        request.send(data);
        return false;
    };

    // send selected vehicle to remove to server.
    document.querySelector('#veh_sel').onsubmit = () => {
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/veh_delete');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        // Callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success) {
                alert(`"Vehicle deleted successfully`);
                document.querySelector('#veh_close').click();
            }
            else {
                alert("oops something went wrong. Please reload dashboard and try again");
            }
        };
        const data = new FormData();
        var id_sel_veh = document.querySelector('#id_sel_veh').value;
        data.append('id_sel_veh', id_sel_veh);
        data.append('meta', 2);
        request.send(data);
        return false;
    };

    // details
    document.querySelector('#acct_details').onsubmit = () => {
        var cookies = parse_cookies();
        const request = new XMLHttpRequest();
        request.open('POST', '/details');
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);

        //callback
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            console.log(data);
            var len = data.data.length;
            document.querySelector('#details_close').click();
            if (len > 0) {
                const template = Handlebars.compile(document.querySelector('#details_script').innerHTML);
                var name = data.data[0].name;
                var owner = data.data[0].owner;
                var phone = data.data[0].phone;
                var email = data.data[0].email;
                var address = data.data[0].address;
                let content = template({'name': name, 'owner': owner, 'phone': phone, 'email': email, 'address': address});
                document.querySelector('#content_block').innerHTML += content;
            }
            else {
                alert("looks like there was an error.  Please reload dashboard.");
            }
        };
        const data = new FormData();
        var id_of_accounts = document.querySelector('#id_of_accounts').value;
        data.append('id_of_accounts', id_of_accounts);
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
