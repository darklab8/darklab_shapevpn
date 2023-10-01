package backUtils

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Helloworld godoc
// @Summary ping helloworld
// @Schemes
// @Description do ping
// @Tags ping
// @Accept json
// @Produce json
// @Success 200 {string} Helloworld
// @Router /example/helloworld [get]
func Helloworld(g *gin.Context) {
	g.JSON(http.StatusOK, "helloworld")
}

type Pong struct {
	Message string `json:"message" example:"pong"`
}

// Ping godoc
// @Tags ping
// @Produce json
// @Success 200 {object} Pong
// @Router /ping [get]
func Ping(c *gin.Context) {
	c.JSON(http.StatusOK, &Pong{Message: "pong"})
}
