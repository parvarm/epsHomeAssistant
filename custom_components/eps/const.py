"""Constants for the EPS integration."""
from pyepsalarm import EPS
from homeassistant.components.alarm_control_panel import AlarmControlPanelState

DOMAIN = "eps"
DATA_COORDINATOR = "eps"

EPS_TO_HASS = {
    EPS.ARMED_AWAY: AlarmControlPanelState.ARMED_AWAY,
    EPS.ARMED_NIGHT: AlarmControlPanelState.ARMED_NIGHT,
    EPS.DISARMED: AlarmControlPanelState.DISARMED,
    EPS.TRIGGERED: AlarmControlPanelState.TRIGGERED,
}
