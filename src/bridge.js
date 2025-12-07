window.addEventListener('pywebviewready', function() {
    window.runpyfn = function runpyfn(function_name, ...args) {
        return pywebview.api.runfn(function_name, ...args);
    }
});