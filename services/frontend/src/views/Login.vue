<template>
<v-container>
    <h1>{{ message }}</h1>
    <v-card
      flat
      class="mx-auto my-12"
      :max-width="400"
    >
        <div class="login">
           <div
            align
          >
            <v-form
              ref="form"
              v-model="validForm"
              lazy-validation
              @keyup.enter="clickLogin"
            >
              <v-text-field
                v-model="form.username"
                label="User"
                :rules="formRules.username"
                required
              />
              <v-text-field
                v-model="form.password"
                label="Password"
                :rules="formRules.password"
                required
                :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'visibility' : 'visibility_off'"
              />
            </v-form>
          </div>
        </div>
      <v-card-actions class="login">
        <v-btn
          block
          :disabled="!validForm"
          @click.stop="clickLogin"
        >
          Login
        </v-btn>
      </v-card-actions>
    </v-card>
</v-container>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Login',
  data() {
    return {
      message: '',
      validForm: true,
      form: {
        username: null,
        password: null,
      },
      formRules: {
        username: [
          v => !!v || 'Required field'
        ],
        password: [
          v => !!v || 'Required field'
        ]
      },
      showPassword: false,
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async clickLogin() {
      const User = new FormData()
      User.append('username', this.form.username)
      User.append('password', this.form.password)
      await this.logIn(User)
      this.$router.push('/dashboard')
    }
  }
}
</script>
