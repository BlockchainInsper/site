function loadMembers() {


    members = document.createElement("div")


    members.class = "flex-container"

    members.id = "members"


    $.getJSON("js/config/members.json", function (json) {
        $.get("https://api.github.com/orgs/BlockchainInsper/public_members", function (data) {

            

            for (let index = 0; index < data.length; index++) {

            for (let index = 0; index < data.length; index++) {



                let { login, avatar_url } = data[index]
                position = "Tech Member"

                let { login, avatar_url } = data[index]
                position = "Tech Member"

                if (json[login] == undefined) {

                    template = `<div id="${login}" class="box";">
                                    <div class="image-round">
                                        <img src="${avatar_url}" alt="${login}">
                                    </div>
                                    <h3 id="name">${login}</h3>
                                    <p id="position">${position}</p>
                                </div>`
                } else {
                    json[login].seen = true
                    template = `<div id="${login}" class="box";">
                                    <div class="image-round">
                                        <img src="${json[login].img}" alt="${login}">
                                    </div>
                                    <h3 id="name">${login}</h3>
                                    <p id="position">${json[login].position}</p>
                                </div>`
                }





                let user = document.createElement("div");
                user.innerHTML = template
                members.appendChild(user.firstChild)


               






        });


        Object.keys(json).forEach(key => {
            let obj = json[key]
            if (obj.seen == undefined) {


                let template = `<div id="${obj.name}" class="box";">
                                    <div class="image-round">
                                        <img src="${obj.img}" alt="${obj.name}">
                                    </div>
                                    <h3 id="name">${obj.name}</h3>
                                    <p id="position">${obj.position}</p>
                                </div>`

                let user = document.createElement("div");
                user.innerHTML = template
                members.appendChild(user.firstChild)
            }





        });



                let user = document.createElement("div");
                user.innerHTML = template
                members.appendChild(user.firstChild)


            }



        });
    });







    return members;

}
