const form = document.getElementById('uploadForm');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById('csvFile');
  if (!fileInput.files.length) return alert('Please upload a CSV');

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  try {
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    document.getElementById('result').innerText = JSON.stringify(data.prediction, null, 2);
  } catch (err) {
    document.getElementById('result').innerText = 'Error connecting to backend.';
  }
});