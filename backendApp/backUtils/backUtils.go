package backUtils

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Pong struct {
	Message string `json:"message"`
}

// @Produce json
// @Success 200 {object} Pong
// @Router /ping [get]
func Ping(c *gin.Context) {
	c.JSON(http.StatusOK, &Pong{Message: "pong"})
}
