const state = {
  notes: [],
};

const actions = {
  // action to send note to backend
  addNote({ commit }, note) {
    commit("ADD_NOTE", note);
  },
};

const mutations = {
  // mutation to add not to state
  ADD_NOTE(state, payload) {
    state.notes.push(payload);
  },
};

const getters = {
  notes: (state) => state.notes,
};

const noteTakingModule = {
  state,
  actions,
  mutations,
  getters,
};

export default noteTakingModule;
