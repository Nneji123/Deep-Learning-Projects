    var ctx = document.getElementById('chartEmail').getContext('2d');
    var myPieChart = new Chart(ctx, {
      type: 'pie',
      data: {
        datasets: [{
          data: [10, 20, 30]
        }],
        labels: [
          'Red',
          'Yellow',
          'Blue'
        ]
      },
      options: {}
    });
