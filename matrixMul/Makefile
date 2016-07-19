BENCHMARK = matrixMul

SRCDIR = src
OBJDIR = obj
BINDIR = bin

SRC = $(SRCDIR)/matrixMul.cu
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(SRC))
BIN = $(BINDIR)/$(BENCHMARK)
CMD = ./$(BENCHMARK) -wA=64 -hA=64 -wB=128 -hB=64 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

include ../common.mk

