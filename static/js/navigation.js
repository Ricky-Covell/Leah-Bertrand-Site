const bgImg1 = document.getElementById('background-img-1')
const bgImg2 = document.getElementById('background-img-2')
const bgImg3 = document.getElementById('background-img-3')
const hintText = document.getElementById('hintText');
const navLeah = document.getElementById('nav-leah');
const worksDropdownContainer = document.getElementById("worksDropdownContainer")
const worksIndexContainer = document.getElementById("works-index-container");
const showWorkArea = document.getElementById('showWorkArea')
const worksNavItem = document.getElementById("worksNavItem")
const workDropdownClass = document.getElementsByClassName('worksDropdownTest')
const workDropdownHover = document.getElementById('worksDropdownHover')
const workCardLinks = document.getElementsByClassName("works-card-link");
const performancesCardLinks = document.getElementsByClassName("performances-card-link");
const testingDiv = document.getElementById("testing");
const workContainers = document.getElementsByClassName("show-work-container");
const workCards = document.getElementsByClassName('work-cards');
const showWorkContainerImg = document.getElementsByClassName('show-work-img-container');
const aboutArea = document.getElementById('aboutContainer');
const navAbout = document.getElementById('navAbout');

const performancesDropdownContainer = document.getElementById('performancesDropdownContainer');
const performancesIndexContainer = document.getElementById('performances-index-container');
const showPerformanceArea = document.getElementById('showPerformanceArea');
const performancesContainer = document.getElementsByClassName('show-performance-container');
const performancesDropdownHover = document.getElementById("performancesDropdownHover")

// Hides hint when page is clicked anywhere

document.addEventListener('mousedown', (evt) => {
    hintText.hidden = true;
})

    // Show start screen when Leah Bertrand is clicked
navLeah.addEventListener('click', (evt) => {
    evt.preventDefault()

    worksDropdownContainer.classList.add('d-none')
    worksDropdownContainer.classList.remove('d-block')
    performancesDropdownContainer.classList.add('d-none')
    performancesDropdownContainer.classList.remove('d-block')
    showWorkArea.classList.add('d-block')
    showWorkArea.classList.remove('d-none')
    showPerformanceArea.classList.add('d-none')
    showPerformanceArea.classList.remove('d-block')
    Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
    Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
    Array.from(performancesContainer).forEach((div) => {div.classList.add('d-none')})
    Array.from(performancesContainer).forEach((div) => {div.classList.remove('d-block')})
    aboutArea.classList.add('d-none')
    aboutArea.classList.remove('d-block')
})

// Allows works index container to be scrolled through horizonally with mouse wheel when hovered over
Array.from(showWorkContainerImg).forEach((container) => container.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    container.scrollLeft += evt.deltaY;
}));
                    

// Adds event listener to Works button that displays work dropdown when clicked
workDropdownHover.addEventListener('click', (evt) => {
    evt.preventDefault()

    worksDropdownContainer.classList.add('d-block')
    worksDropdownContainer.classList.remove('d-none')
    performancesDropdownContainer.classList.add('d-none')
    performancesDropdownContainer.classList.remove('d-block')
    showWorkArea.classList.add('d-block')
    showWorkArea.classList.remove('d-none')
    showPerformanceArea.classList.add('d-none')
    showPerformanceArea.classList.remove('d-block')
    Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
    Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
    Array.from(performancesContainer).forEach((div) => {div.classList.add('d-none')})
    Array.from(performancesContainer).forEach((div) => {div.classList.remove('d-block')})
    aboutArea.classList.add('d-none')
    aboutArea.classList.remove('d-block')

})

// Adds event listener to Performances button that displays performance dropdown when clicked
performancesDropdownHover.addEventListener('click', (evt) => {
    evt.preventDefault()

    performancesDropdownContainer.classList.add('d-block')
    performancesDropdownContainer.classList.remove('d-none')
    worksDropdownContainer.classList.add('d-none')
    worksDropdownContainer.classList.remove('d-block')
    showPerformanceArea.classList.add('d-block')
    showPerformanceArea.classList.remove('d-none')
    showWorkArea.classList.add('d-none')
    showWorkArea.classList.remove('d-block')
    Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
    Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
    Array.from(performancesContainer).forEach((div) => {div.classList.add('d-none')})
    Array.from(performancesContainer).forEach((div) => {div.classList.remove('d-block')})
    aboutArea.classList.add('d-none')
    aboutArea.classList.remove('d-block')

})

// Adds event listener to each artwork link, prevents redirect, and adds html of artwork documentation dynamically
let workContainersArray = Array.from(workContainers);
Array.from(workCardLinks)
    .forEach((link) => link.addEventListener('click', (evt) => {
        evt.preventDefault();
        

        worksDropdownContainer.classList.add('d-none')
        worksDropdownContainer.classList.remove('d-block')
        workContainersArray.forEach(function (card) {
            card.classList.add('d-none')
            card.classList.remove('d-block')
        })

        let workID = link.dataset.workid;
        let workPage = document.getElementById(`display-work-${workID}`);
        workPage.classList.add('d-block')
        workPage.classList.remove('d-none')
    }))




let performancesContainersArray = Array.from(performancesContainer);
Array.from(performancesCardLinks)
    .forEach((link) => link.addEventListener('click', (evt) => {
        evt.preventDefault();
        

        performancesDropdownContainer.classList.add('d-none')
        performancesDropdownContainer.classList.remove('d-block')
        performancesContainersArray.forEach(function (card) {
            card.classList.add('d-none')
            card.classList.remove('d-block')
        })

        let performanceID = link.dataset.performanceid;
        let performancePage = document.getElementById(`display-performance-${performanceID}`);
        performancePage.classList.add('d-block')
        performancePage.classList.remove('d-none')
    }))



// ABOUT PAGE HANDLING
navAbout.addEventListener('click', (evt) => {
    evt.preventDefault()

    worksDropdownContainer.classList.add('d-none')
    worksDropdownContainer.classList.remove('d-block')
    Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
    Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
    Array.from(performancesContainer).forEach((div) => {div.classList.add('d-none')})
    Array.from(performancesContainer).forEach((div) => {div.classList.remove('d-block')})
    showWorkArea.classList.add('d-none')
    showWorkArea.classList.remove('d-block')
    performancesDropdownContainer.classList.add('d-none')
    performancesDropdownContainer.classList.remove('d-block')
    showPerformanceArea.classList.add('d-none')
    showPerformanceArea.classList.remove('d-block')
    aboutArea.classList.add('d-block')
    aboutArea.classList.remove('d-none')

})




                                        // OLD HOVER DROPDOWN SCRIPT

    // Adds event listener to Works Dropdown Container that handles dropdown behavior when hovering over "Works" nav item
                // workDropdownHover.addEventListener('mouseenter', (evt) => {

                        // worksDropdownContainer.classList.add('d-block')
                        // worksDropdownContainer.classList.remove('d-none')
                        // Array.from(workContainers).forEach((div) => {div.classList.add('d-none')})
                        // Array.from(workContainers).forEach((div) => {div.classList.remove('d-block')})
                        
                //     })


                // worksDropdownContainer.addEventListener('mouseleave', (evt) => {
                //                     // PROBLEM: 'mouseleave' won't stop triggering on child elements of work dropdown div
                //                     // WORKAROUND: 'mouseleave' triggered after setTimeout func below
                //         let t = null;
                //         t = setTimeout(function() {
                //             worksDropdownContainer.classList.add('d-none')
                //             worksDropdownContainer.classList.remove('d-block')
                //             Array.from(workContainers).forEach((div) => div.style.filter='opacity(100%)')
                //             Array.from(backgroundImgs).forEach((img) => {img.style.filter='blur(0px)'})
                //         }, 100);

                //         worksDropdownContainer.addEventListener('mouseenter', (evt) => {
                //             if(t !== null) {
                //                 clearTimeout(t);
                //                 t = null;
                //             }
                //         })

                //     })


                // workDropdownClassArray = Array.from(workDropdownClass);

                // Array.from(workDropdownClassArray)
                //     .forEach((element) => element.addEventListener('click', (evt) => {

                //         worksDropdownContainer.classList.add('d-none')
                //         worksDropdownContainer.classList.remove('d-block')
                //         Array.from(workContainers).forEach((div) => div.style.filter='opacity(100%)')
                //         Array.from(backgroundImgs).forEach((img) => {img.style.filter='blur(0px)'})
                //     }))