const labels = {{labels | safe }};

            const data = {
                labels: labels,
                datasets: [{
                        label: 'Completed Registrations',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: {{data_true_count | safe}},
                        fill: false,
                        pointStyle: 'recRot',
                        pointRadius: 5,
                        pointHoverRadius: 10
                    },
                    {
                        label: 'Total Registrations',
                        backgroundColor: 'rgb(0, 0, 205)',
                        borderColor: 'rgb(0, 0, 205)',
                        data: {{data_total_count | safe}},
                        fill: false,
                        pointStyle: 'circle',
                        pointRadius: 10,
                        pointHoverRadius: 15
                    },

                ]
            };


            const actions = [{
                name: 'pointStyle: rectRounded',
                handler: (chart) => {
                    chart.data.datasets.forEach(dataset => {
                        dataset.pointStyle = 'rectRounded';
                    });
                    chart.update();
                }
            }, ]


            const config = {
                type: 'line',
                data: data,
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                            text: 'Registrations For Each Week'
                        },
                    }
                },
            };


            const myChart = new Chart(
                document.getElementById('myChart'),
                config
            );