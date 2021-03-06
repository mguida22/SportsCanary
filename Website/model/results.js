var mongoose = require('mongoose');

var resultSchema = new mongoose.Schema({
    sport_type: String,
    event_name: String,
    score_applicable: Boolean,
    score_1: Number,
    score_2: Number,
    team_1_percentage_win: Number,
    team_2_percentage_win: Number,
    event_date: { type: Date, default: Date.now }
});
mongoose.model('Result', resultSchema);