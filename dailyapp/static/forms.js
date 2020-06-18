var weight_form = document.getElementById('weight');
weight_form.addEventListener("submit", function(e) {
    e.preventDefault();
    if (this.weight.value > 0) {
        this.submit();
    }
    else {
        alert('Weight has to be higher than 0!');
    };
}, false);

var training_form = document.getElementById('training');
training_form.addEventListener("submit", function(e) {
    e.preventDefault();
    var elements = this.elements;
    var valid_status = true;
    for (var i = 1; i < elements.length - 1; i++) {
        var el = elements[i].value;
        if (el < 0) {
            valid_status = false;
        }
    }
    if (valid_status) {
        training_form.submit();
    }
    else {
        alert('Wszystkie ciezary muszy byc wieksze od 0!');
    }
}, false);