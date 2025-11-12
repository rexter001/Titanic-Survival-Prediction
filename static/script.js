document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const pclass = document.getElementById('pclass').value;
    const sex = document.getElementById('sex').value;
    const age = document.getElementById('age').value;
    const sibsp = document.getElementById('sibsp').value;
    const parch = document.getElementById('parch').value;
    const fare = document.getElementById('fare').value;
    const embarked = document.getElementById('embarked').value;
    
    const form = document.getElementById('predictionForm');
    const result = document.getElementById('result');
    const loading = document.getElementById('loading');
    const resultContent = document.getElementById('resultContent');
    
    // Show loading state
    form.style.display = 'none';
    loading.classList.remove('hidden');
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                pclass: parseInt(pclass),
                sex: parseInt(sex),
                age: parseInt(age),
                sibsp: parseInt(sibsp),
                parch: parseInt(parch),
                fare: parseFloat(fare),
                embarked: parseInt(embarked)
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            const survives = data.result.includes('Likely');
            const resultClass = survives ? 'result-survive' : 'result-perish';
            
            resultContent.innerHTML = `
                <div class="result-item">
                    <div class="result-label">Prediction</div>
                    <div class="result-value ${resultClass}">${data.result}</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Survival Probability</div>
                    <div class="result-value">${data.survival_probability}%</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Confidence</div>
                    <div class="result-value">${data.confidence}%</div>
                </div>
                <hr style="margin: 15px 0; border: none; border-top: 1px solid #ddd;">
                <div style="font-size: 12px; color: #999;">
                    <strong>Input:</strong> Class=${pclass}, Sex=${sex ? 'Male' : 'Female'}, 
                    Age=${age}, Fare=£${fare}, Family=${parseInt(sibsp)+parseInt(parch)}, Port=${embarked}
                </div>
            `;
            
            result.classList.remove('hidden');
        } else {
            resultContent.innerHTML = `<p style="color: #e74c3c;">Error: ${data.error}</p>`;
            result.classList.remove('hidden');
        }
    } catch (error) {
        resultContent.innerHTML = `<p style="color: #e74c3c;">Error: ${error.message}</p>`;
        result.classList.remove('hidden');
    } finally {
        loading.classList.add('hidden');
    }
});

function resetForm() {
    document.getElementById('predictionForm').reset();
    document.getElementById('result').classList.add('hidden');
    document.getElementById('predictionForm').style.display = 'block';
}
