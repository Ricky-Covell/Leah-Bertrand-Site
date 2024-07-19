const stylehere = document.getElementById('stylesheet');
const fuschiaMaxScript = '<link rel="stylesheet" href="/static/fuschiaMax.css">'
const blueMaxScript = '<link rel="stylesheet" href="/static/blueMax.css">'

document.getElementById('fuschiaMax').addEventListener('click', (evt) => {
    stylehere.innerHTML = fuschiaMaxScript
})

document.getElementById('blueMax').addEventListener('click', (evt) => {
    stylehere.innerHTML = blueMaxScript
    console.log('sodiguhn')
})