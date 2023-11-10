document.addEventListener('DOMContentLoaded', function () {
    // Navbar initialization
    let navbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(navbar);

    // Select initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    // datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {format: "yyyy-mm-dd"});
});