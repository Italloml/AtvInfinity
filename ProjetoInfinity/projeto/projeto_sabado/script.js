const listaTarefas = document.getElementById('lista-tarefas')
const semTarefas = document.getElementById('sem-tarefas')
const contadorTarefas = document.getElementById('contador-tarefas')
const btnInfo = document.getElementById('btnCaptura')

semTarefas.style.display = "none"

btnInfo.addEventListener('click', (e) => {
    e.preventDefault()
    const novaTarefa = document.createElement('li')
    novaTarefa.innerHTML = `
        <input type="checkbox">
        <span class="tarefa-Texto">Nova Tarefa</span>
        <button>Excluir</button>
`
    listaTarefas.appendChild(novaTarefa)
    
})



contadorTarefas.innerText = `Total de Tarefas: ${listaTarefas.children.length - 1}`