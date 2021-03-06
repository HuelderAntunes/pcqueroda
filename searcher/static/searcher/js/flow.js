var state = {
  activeStep: $(".steps-wrapper .step .active").data("step"),
  softwares: {},
  type: "Desktop",
};

function getResults() {
  $(".results .rs-card-list").empty();
  $(".results .rs-card.big").empty();
  $(".results .rs-card-list").hide();
  $(".results .rs-card.big").hide();
  $(".results .error").hide();
  $(".results h4").hide();
  $(".results .loading").show();

  $.ajax({
    url:
      "/" +
      "results?sw=" +
      Object.values(state.softwares).join("&sw=") +
      "&category=" +
      state.type,

    success: function (data) {
      $(".results .loading").hide();
      $(".results .error").hide();
      if (data["success"]["computer_list"].length == 0) {
        $(".results .error").fadeIn();
      } else {
        $(".results .rs-card-list").fadeIn();
        $(".results .rs-card.big").fadeIn();
        if (data["success"]["computer_list"].length > 1) {
          $(".results h4").fadeIn(1000);
        }

        var featured = data["success"]["computer_list"][0];
        $(".results .rs-card.big")
          .append(
            ` <img
      src="${
        !featured.fields.image.includes("https")
          ? "https://storage.googleapis.com/pcqueroda-images/" +
            featured.fields.image
          : featured.fields.image
      }"
      alt="${featured.fields.title}"
    />
    <div class="description">
      <span class="label label-primary">Roda no Médio</span>
      <h3>R$ ${featured.fields.price.toLocaleString("pt-br")}</h3>
      <p>
        ${featured.fields.title}
      </p>
      <a href="${featured.fields.affiliate_link}" target="_blank">VER MAIS</a>
    </div>`
          )
          .hide()
          .fadeIn();

        data["success"]["computer_list"]
          .slice(1)
          .map(function (computer, index) {
            $(".results .rs-card-list")
              .append(
                `<li class="rs-card small">

        <img
          src="${
            !computer.fields.image.includes("https")
              ? "https://storage.googleapis.com/pcqueroda-images/" +
                computer.fields.image
              : computer.fields.image
          }"
          alt="${computer.fields.title}"
        />
        <div class="description">
        <span class="label label-primary">${
          !index ? "Roda no Mínimo" : "Roda no Ultra"
        }</span>
          <h3>R$ ${computer.fields.price.toLocaleString("pt-br")}</h3>
          <p>
            ${computer.fields.title}
          </p>
          <a href="${
            computer.fields.affiliate_link
          }" target="_blank">VER MAIS</a>
        </div>
      </li>`
              )
              .hide()
              .fadeIn();
          });
      }
    },
  });
}

function showStep(step) {
  if (Object.keys(state.softwares).length > 0) {
    $(".search-next button.disabled").removeClass("disabled");
  } else {
    $(".search-next button").addClass("disabled");
  }

  if (
    $(".steps-wrapper .step .step-item[data-step]").length - 1 !==
    state.activeStep
  ) {
    $(".search-next button").show();
  } else {
    $(".search-next button").hide();

    if (!localStorage["mailprompt"]) {
      setTimeout(function () {
        $("#mail-prompt").addClass("active");
      }, 3000);
    }

    getResults();
  }

  if (state.activeStep === 0) {
    $(".search-next .back-link").hide();
  } else {
    $(".search-next .back-link").show();
  }

  $(".steps-wrapper .step .step-item.active").removeClass("active");
  $(".steps-wrapper .step .step-item[data-step='" + step + "']").addClass(
    "active"
  );
  $(".game-searcher div[data-step").hide();
  $(".game-searcher div[data-step='" + step + "']").fadeIn();
}

function addStepButtonListeners() {
  $(".game-searcher .search-next button").click((e) => {
    showStep(++state.activeStep);
    $("html, body").animate(
      {
        scrollTop: $("#searcher-app").offset().top,
      },
      500
    );
  });

  $(".game-searcher .search-next .back-link").click((e) => {
    showStep(--state.activeStep);
    $("html, body").animate(
      {
        scrollTop: $("#searcher-app").offset().top,
      },
      500
    );
  });
}

function getStatusText() {
  if (Object.keys(state.softwares).length) {
    return `Você selecionou: <span>${Object.keys(state.softwares)
      .map((e) => {
        return `<span class="delete" data-id="${state.softwares[e]}">${e}</span>`;
      })
      .join(", ")
      .replace(/,\s([^,]+)$/, " e $1")}</span>`;
  } else {
    return `Selecione no mínimo um jogo ou software para continuar.`;
  }
}

$(".type-selector ul li").click((e) => {
  $(".type-selector ul li").removeClass("active");

  $(e.target).addClass("active");
  state.type = $(e.target).data("type");

  if (state.type.length > 0) {
    $(".search-next button.disabled").removeClass("disabled");
  } else {
    $(".search-next button").addClass("disabled");
  }
});

function addSoftwareListeners() {
  Object.keys(state.softwares).forEach((element) => {
    $(
      ".software-list ul li[data-id='" + state.softwares[element] + "']"
    ).addClass("active");
  });

  $(".software-list h6").html(getStatusText());

  var clickFunction = function (e) {
    var name = $(e.target).text();

    var li = $(`.software-list ul li[data-id="${state.softwares[name]}"]`);
    li.removeClass("active");
    delete state.softwares[name];
    $(".software-list h6").html(getStatusText());
    $(".software-list h6 .delete").click(clickFunction);
  };

  $(".software-list h6").html(getStatusText());
  $(".software-list h6 .delete").click(clickFunction);

  $(".software-list ul li").click((e) => {
    var li = $(e.target).closest("li");
    if (!li.hasClass("active")) {
      li.addClass("active");

      state.softwares[li.data("name")] = li.data("id");
    } else {
      li.removeClass("active");
      delete state.softwares[li.data("name")];
    }

    if (Object.keys(state.softwares).length > 0) {
      $(".search-next button.disabled").removeClass("disabled");
    } else {
      $(".search-next button").addClass("disabled");
    }

    $(".software-list h6").html(getStatusText());
    $(".software-list h6 .delete").click(clickFunction);
  });
}

addStepButtonListeners();
addSoftwareListeners();
showStep(state.activeStep);
$(".software-list h6").html(getStatusText());
