addEventListener('load', ev=>{ const x = 100, y = 200 })

const toggleDark=()=>{
    const L = document.querySelector("html").classList
    L[L.filter("dark").length?"remove":"add"]("dark")
}
