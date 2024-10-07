function pushIssue(summary, description){
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "oUoksqROt2h9ivjiqw7sTA8S41G8ChLv");
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      "summary": summary,
      "description": description,
      "project": {
        "id": 2
      },
      "category": {
        "id": 1
      },
      "priority": {
        "name": "normal"
      },
      "severity": {
        "name": "trivial"
      },
      "reproducibility": {
        "name": "always"
      }
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://localhost/mantisbt-2.26.2/api/rest/issues", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
}