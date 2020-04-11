
function imageExists(image_url) {

    var http = new XMLHttpRequest();

    http.open('HEAD', image_url, false);
    http.send();

    return http.status != 404;

}


function loadMembers() {


    members = document.createElement("div")


    members.class = "flex-container"

    members.id = "members"



    $.getJSON("js/config/members.json", function (json) {
        $.get("https://api.github.com/orgs/BlockchainInsper/public_members", function (data) {
            //response = JSON.parse() 

            

            for (let index = 0; index < data.length; index++) {

             let template;



                let { login, avatar_url } = data[index]
                position = "Tech Member"

                if (json[login]==undefined){
                    template = `<div id="${login}" class="box";">

                                    <div class="image-round">
                                        <img src="${avatar_url}" alt="Person 1">
                                    </div>
                                    <h3 id="name">${login}</h3>
                                    <p id="position">${position}</p>
                                </div>`
                } else {
                    template = `<div id="${login}" class="box";">
                                    <div class="image-round">
                                        <img src="${json[login].img}" alt="Person 1">
                                    </div>
                                    <h3 id="name">${login}</h3>
                                    <p id="position">${json[login].position}</p>
                                </div>`
                }

               









                let user = document.createElement("div");
                user.innerHTML = template
                members.appendChild(user.firstChild)


            }



        });
    });



    return members;
