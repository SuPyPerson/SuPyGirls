<div id="ident-modal" class="modal">
  <div class="modal-background"></div>
  <div class="modal-content">
    <!-- Any other Bulma elements you want -->
    <form id="ident-form" action="game/__claim/[[project]]" method="POST">
        <div class="field">
          <label class="label">Nome completo</label>
          <div class="control">
            <input class="input" type="text"  name="author_name" placeholder="<Entre aqui o seu nome>">
          </div>
        </div>

        <div class="field">
          <label class="label">Nome Curto de Usuário</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input is-success" type="text" name="author_nick" placeholder="<no máximo 10 letras>">
            <span class="icon is-small is-left">
              <i class="fas fa-user"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-check"></i>
            </span>
          </div>
          <p class="help is-success">Este nome de usuário está disponível</p>
        </div>

        <div class="field">
          <label class="label">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input is-danger" type="email" name="author_email"  placeholder="Email input" value="hello@">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-exclamation-triangle"></i>
            </span>
          </div>
          <p class="help is-danger">Este email é invalido</p>
        </div>
        <!--

        <div class="field">
          <label class="label">Subject</label>
          <div class="control">
            <div class="select">
              <select>
                <option>Select dropdown</option>
                <option>With options</option>
              </select>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label">Message</label>
          <div class="control">
            <textarea class="textarea" placeholder="Textarea"></textarea>
          </div>
        </div>
        -->

        <div class="field">
          <label class="label">Site Da Escola ou do Professor</label>
          <div class="control">
            <input class="input" type="text" name="author_site"  placeholder="http://www.minhaescola...">
          </div>
        </div>

        <div class="field">
          <label class="label">Nome Da Escola</label>
          <div class="control">
            <input class="input" type="text" name="author_org"  placeholder="Escola Municipal..">
          </div>
        </div>

        <div class="field">
          <div class="control">
            <label class="radio label">
              <input type="radio" name="author_public" checked>
              Pública
              </input>
            </label>
            <label class="radio label">
              <input type="radio" name="author_public">
              Privada
              </input>
            </label>
          </div>
        </div>

        <div class="field">
          <div class="control">
            <label class="checkbox label">
              <input type="checkbox">
              Eu concordo com <a href="#">os termos and condições</a>
              </input>
            </label>
          </div>
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Submit</button>
          </div>
          <div class="control">
            <button class="button is-text">Cancel</button>
          </div>
        </div>
      </form>
    </div>
  <button onclick="claim_project('');" class="modal-close is-large" aria-label="close"></button>
</div>


