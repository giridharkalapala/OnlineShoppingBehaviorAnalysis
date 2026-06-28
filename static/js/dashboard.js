document.addEventListener('DOMContentLoaded', () => {
    // Load KPIs
    fetch('/api/kpis').then(res => res.json()).then(data => {
        document.getElementById('kpi-row').innerHTML = `
            <div class="col-md-2"><div class="kpi-card"><h6>Total Customers</h6><h3>${data.total_customers}</h3></div></div>
            <div class="col-md-2"><div class="kpi-card"><h6>Total Orders</h6><h3>${data.total_orders}</h3></div></div>
            <div class="col-md-2"><div class="kpi-card"><h6>Revenue</h6><h3>${data.total_revenue}</h3></div></div>
            <div class="col-md-2"><div class="kpi-card"><h6>AOV</h6><h3>${data.aov}</h3></div></div>
            <div class="col-md-2"><div class="kpi-card"><h6>Top Category</h6><h3>${data.top_category}</h3></div></div>`;
    });

    // Load All 10 Charts
    fetch('/api/charts').then(res => res.json()).then(d => {
        Plotly.newPlot('chart1', [{x: Object.keys(d.age_dist), y: Object.values(d.age_dist), type:'bar', marker:{color:'#38bdf8'}}], {title:'1. Age Distribution', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart2', [{labels: Object.keys(d.gender_purchase), values: Object.values(d.gender_purchase), type:'pie'}], {title:'2. Gender-wise Purchase', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart3', [{x: Object.keys(d.category_pref), y: Object.values(d.category_pref), type:'bar', marker:{color:'#f472b6'}}], {title:'3. Category Preferences', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart4', [{x: Object.keys(d.monthly_trend), y: Object.values(d.monthly_trend), type:'scatter', mode:'lines+markers'}], {title:'4. Monthly Trends', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart5', [{x: ['No Discount','Discount'], y: [d.discount_impact[0], d.discount_impact[1]], type:'bar'}], {title:'5. Discount Impact', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart6', [{x: Object.keys(d.ratings_purchase), y: Object.values(d.ratings_purchase), type:'bar'}], {title:'6. Ratings vs Purchase', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart7', [{labels: Object.keys(d.payment_method), values: Object.values(d.payment_method), type:'pie'}], {title:'7. Payment Method', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart8', [{x: Object.keys(d.spending_pattern), y: Object.values(d.spending_pattern), type:'bar'}], {title:'8. Spending by Age', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart9', [{x: Object.keys(d.top_selling), y: Object.values(d.top_selling), type:'bar'}], {title:'9. Top-Selling Categories', paper_bgcolor:'transparent', font:{color:'white'}});
        Plotly.newPlot('chart10', [{x: Object.keys(d.segmentation), y: Object.values(d.segmentation), type:'box'}], {title:'10. Customer Segmentation', paper_bgcolor:'transparent', font:{color:'white'}});
    });
});