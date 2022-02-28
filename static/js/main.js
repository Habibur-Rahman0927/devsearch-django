let searchForm = document.querySelector('#searchForm')
let pageLinks = document.getElementsByClassName('btn--link')

if(searchForm){
  for (let page = 0; page < pageLinks.length; page++) {
    pageLinks[page].addEventListener('click', function(e){
      e.preventDefault()
      let page = this.dataset.page
      searchForm.innerHTML += `<input value=${page} name="page" hiddin/>`
      searchForm.submit()
    })
    
  }
}