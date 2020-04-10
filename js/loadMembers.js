function loadMembers() {


    members = document.createElement("div")


    members.class = "flex-container"

    members.id = "members"


    $.get("https://api.github.com/orgs/BlockchainInsper/public_members", function (data) {
        //response = JSON.parse() 



        for (let index = 0; index < data.length; index++) {




            let { login, avatar_url } = data[index]

            position = "Babaca"

            let template = `<div id="${login}" class="box";">
                                <div class="image-round">
                                    <img src="${avatar_url}" alt="Person 1">
                                </div>
                                <h3 id="name">${login}</h3>
                                <p id="position">${position}</p>
                            </div>`





            let user = document.createElement("div");
            user.innerHTML = template
            members.appendChild(user.firstChild)

            
        }



    });

    return members;
    
}