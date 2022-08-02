const labels = ["Agadez","Diffa","Dosso","Maradi","Niamey","Tahoua","Tillaberi","Zinder"];

const data = {
    labels: labels,
    datasets: [
        {
            label: 'Élections Présidentielles',
            backgroundColor: 'rgb(255, 99, 132,.4)',
            borderColor: 'rgb(255, 99, 132)',
            data: E1,
            pointStyle: 'circle',
            pointRadius: 5,
            pointHoverRadius: 8,
            tension: 0.2
        },
        {
            label: 'Élections Législatives',
            backgroundColor: 'rgb(62, 196, 44,.4)',
            borderColor: 'rgb(62, 196, 44)',
            data: E2,
            pointStyle: 'circle',
            pointRadius: 5,
            pointHoverRadius: 8,
            tension: 0.2
        }
    ]
};

const config = {
    type: 'line',
    data: data,
    options: {}
};

const data2 = {
labels: [
    'Élections Présidentielles',
    'Élections Législatives'
],
datasets: [{
    label: 'Election.One',
    data: E3,
    backgroundColor: [
    'rgb(255, 99, 132)',
    'rgb(62, 196, 44)'
    ],
    hoverOffset: 4
}]
};

const config2 = {
type: 'doughnut',
data: data2,
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);

const myPie = new Chart(
    document.getElementById('myPie'),
    config2
);