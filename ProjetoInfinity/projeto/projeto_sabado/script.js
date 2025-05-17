const listaTarefas = document.getElementById('lista-tarefas')
const semTarefas = document.getElementById('sem-tarefas')
const contadorTarefas = document.getElementById('contador-tarefas')
const btnAdd = document.getElementById('btn-adicionar')

function excluirTarefas(e) {
    listaTarefas.removeChild(e.target.parentElement)
    const tamanhoUL = listaTarefas.children.length
    if(tamanhoUL === 1) {
        semTarefas.style.display = 'none'
    }
}
btnAdd.addEventListener('click', (e) => {
    semTarefas.style.display = 'none'
    e.preventDefault()
    const novaTarefa = document.createElement('li')
    novaTarefa.className = 'tarefa'
    novaTarefa.innerHTML = `
        <input type="checkbox" class="checkbox-tarefa">
        <span class="tarefa-Texto">${input.value}{</span>
        <button onclic=excluirTarefas(event) class="btn-excluir">Excluir</button>
    `
    listaTarefas.appendChild(novaTarefa)
    input.value = ''
    input.focus()
})
console.dir(input)

contadorTarefas.innerText = `Total de Tarefas: ${listaTarefas.children.length - 1}`

// incompleto