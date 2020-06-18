window.onload = function () {
    let weight_points = [];
    for (const [week, value] of Object.entries(weight_data)) {
        weight_points.push({ label: `${week}`, y: value});
    }
    var weightChart = new CanvasJS.Chart("weightChartContainer", {
        animationEnabled: true,
        data: [              
        {
            type: "line",
            dataPoints: weight_points
        }
        ]
    });
    weightChart.render();

}

function displayExercise() {
    let exercise_points = [];
    for (const [date, value] of Object.entries(exercise_data)) {
        if (value[1]) {
            exercise_points.push({ label: `${date}` + `, ${value[1]}`, y: value[0] })
        }
    else {
        exercise_points.push({ label: `${date}`, y: value[0] })
    }
    }
    var exerciseChart = new CanvasJS.Chart("exerciseChartContainer", {
        animationEnabled: true,
        title : {
            text: exercise
        },
        data: [              
        {
            type: "line",
            dataPoints: exercise_points
        }
        ]
    });
    exerciseChart.render();
}

displayExercise();

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});
