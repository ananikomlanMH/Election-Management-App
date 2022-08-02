// setTimeout(function(){
//     $('.loader').fadeToggle();
// }, 1000);

// dropdown filter drop
window.addEventListener("click", (e)=>{
    if(!e.target.matches('.show-dropdown  .default_option')){
        if(document.querySelector(".show-dropdown .default_option + ul").classList.contains("active")){
            document.querySelector(".show-dropdown .default_option + ul").classList.remove("active");
        }
    }
    if(!e.target.matches('.dropdown .default_option')){
        if(document.querySelector(".dropdown .default_option + ul").classList.contains("active")){
            document.querySelector(".dropdown .default_option + ul").classList.remove("active");
        }
    }
    if(!e.target.matches('.icon.fi-rr-menu-dots-vertical')){
        table_drop_action.forEach(elm =>{
            if(elm.classList.contains("active")){
                elm.classList.remove("active");
            }
        });
    }
    if(!e.target.matches('.show-type .default_option')){
        if(document.querySelector(".show-type .default_option + ul").classList.contains("active")){
            document.querySelector(".show-type .default_option + ul").classList.remove("active");
        }
    }
    if(!e.target.matches('.show-proc .default_option')){
        if(document.querySelector(".show-proc .default_option + ul").classList.contains("active")){
            document.querySelector(".show-proc .default_option + ul").classList.remove("active");
        }
    }
    if(!e.target.matches('.show-voix .default_option')){
        if(document.querySelector(".show-voix .default_option + ul").classList.contains("active")){
            document.querySelector(".show-voix .default_option + ul").classList.remove("active");
        }
    }
});
window.addEventListener("click", (e)=>{
    if(!e.target.matches('.icon.fi-rr-menu-dots-vertical')){
        table_drop_action.forEach(elm =>{
            if(elm.classList.contains("active")){
                elm.classList.remove("active");
            }
        });
    }
    if(!e.target.matches('.show-groupAction .default_option')){
        if(document.querySelector(".show-groupAction .default_option + ul").classList.contains("active")){
            document.querySelector(".show-groupAction .default_option + ul").classList.remove("active");
        }
    }
});


//Side bar close
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#close-nav");

closeBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function menuBtnChange() {
    if(sidebar.classList.contains("open")){
        closeBtn.classList.replace("fi-rr-menu-burger", "fi-rr-align-right");
    }else {
        closeBtn.classList.replace("fi-rr-align-right","fi-rr-menu-burger");
    }
}

//table
let table_drop_action = document.querySelectorAll('.table_drop_action');
table_drop_action.forEach(element => {
    element.addEventListener("click", ()=>{
        table_drop_action.forEach(elm =>{
            if(elm.classList.contains("active") && elm!=element){
                elm.classList.remove("active");
            }
        });
        element.classList.toggle("active");
    });
});

let filterDrop = document.querySelector(".dropdown .default_option");
let filterElm = document.querySelector(".dropdown .default_option + ul");
filterDrop.addEventListener("click", ()=>{
    filterElm.classList.toggle("active");
});

//show entries
let showDrop = document.querySelector(".show-dropdown .default_option");
let showElm = document.querySelector(".show-dropdown .default_option + ul");
showDrop.addEventListener("click", ()=>{
    showElm.classList.toggle("active");
});

//type
let showDropType = document.querySelector(".show-type .default_option");
let showElmType = document.querySelector(".show-type .default_option + ul");
showDropType.addEventListener("click", ()=>{
    showElmType.classList.toggle("active");
});

//proc
let showDropProc = document.querySelector(".show-proc .default_option");
let showElmProc = document.querySelector(".show-proc .default_option + ul");
showDropProc.addEventListener("click", ()=>{
    showElmProc.classList.toggle("active");
});

//voix
let showDropVoix = document.querySelector(".show-voix .default_option");
let showElmVoix = document.querySelector(".show-voix .default_option + ul");
showDropVoix.addEventListener("click", ()=>{
    showElmVoix.classList.toggle("active");
});

function popUp(){
    const pop = document.querySelector(".popUp_section");
    const form = pop.querySelector("form");
    pop.classList.toggle("active");
    form.reset();
}

function popEdit(id){
    const pop = document.querySelector(".popUp_section.editId"+id);
    pop.classList.toggle("active");
}