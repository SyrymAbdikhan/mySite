function add(name, value) {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set(name, value);
    window.location.search = urlParams;
}