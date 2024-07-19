const bgImg1 = document.getElementById('background-img-1')
const bgImg2 = document.getElementById('background-img-2')
const bgImg3 = document.getElementById('background-img-3')
const worksDropdownContainer = document.getElementById("worksDropdownContainer")
const worksIndexContainer = document.getElementById("works-index-container");
const showWorkArea = document.getElementById('showWorkArea')
const worksNavItem = document.getElementById("worksNavItem")
const workDropdownClass = document.getElementsByClassName('worksDropdownTest')
const workDropdownHover = document.getElementById('worksDropdownHover')
const cardLinks = document.getElementsByClassName("card-link");
const testingDiv = document.getElementById("testing");
const workContainers = document.getElementsByClassName("show-work-container");
const workCards = document.getElementsByClassName('work-cards');
const anotherDropdownDiv = document.getElementById('anotherDropdownDiv');




// Allows works index container to be scrolled through horizonally with mouse wheel when hovered over
worksIndexContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    worksIndexContainer.scrollLeft += evt.deltaY;
});


// Adds event listener to Works Dropdown Container that handles dropdown behavior when hovering over "Works" nav item
workDropdownHover.addEventListener('mouseenter', (evt) => {

        worksDropdownContainer.classList.add('d-block')
        worksDropdownContainer.classList.remove('d-none')
        Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
        Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
        
    })


worksDropdownContainer.addEventListener('mouseleave', (evt) => {
                    // PROBLEM: 'mouseleave' won't stop triggering on child elements of work dropdown div
                    // WORKAROUND: 'mouseleave' triggered after setTimeout func below
        let t = null;
        t = setTimeout(function() {
            worksDropdownContainer.classList.add('d-none')
            worksDropdownContainer.classList.remove('d-block')
            Array.from(workContainers).forEach((div) => div.style.filter='opacity(100%)')
            Array.from(backgroundImgs).forEach((img) => {img.style.filter='blur(0px)'})
        }, 100);

        worksDropdownContainer.addEventListener('mouseenter', (evt) => {
            if(t !== null) {
                clearTimeout(t);
                t = null;
            }
        })

    })


workDropdownClassArray = Array.from(workDropdownClass);

Array.from(workDropdownClassArray)
    .forEach((element) => element.addEventListener('click', (evt) => {

        worksDropdownContainer.classList.add('d-none')
        worksDropdownContainer.classList.remove('d-block')
        Array.from(workContainers).forEach((div) => div.style.filter='opacity(100%)')
        Array.from(backgroundImgs).forEach((img) => {img.style.filter='blur(0px)'})
    }))
    


// Adds event listener to each artwork link, prevents redirect, and adds html of artwork documentation dynamically
workContainersArray = Array.from(workContainers);
Array.from(cardLinks)
    .forEach((link) => link.addEventListener('click', (evt) => {
        evt.preventDefault();
        
        workContainersArray.forEach(function (card) {
            card.classList.add('d-none')
            card.classList.remove('d-block')
        })

        let workID = link.dataset.workid;
        let workPage = document.getElementById(`display-${workID}`);
        workPage.classList.add('d-block')
        workPage.classList.remove('d-none')
    }))




