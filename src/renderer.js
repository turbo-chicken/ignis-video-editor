const information = document.getElementById('info')
information.innerText = `This app is using Node.js (v${versions.node()}), and Electron (v${versions.electron()})`

function getData(){
    console.log('Called!!!');
}

document.querySelector('#btnED').addEventListener('click', () => {
    getData()
})
